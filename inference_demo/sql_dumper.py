import pandas as pd
import xml.etree.ElementTree as ET
import csv
import os
from sqlalchemy import create_engine


def str2int(s):
    return int(float(s))


def create_csv(xml_file, gps_csv, video_file, out_path):
   
    tree = ET.parse(xml_file)
    root = tree.getroot()
    damage_mapping = {'zero':0, 'light':1, 'medium':2, 'high':3, 'non_recoverable':4}
    
    gps = csv.reader(open(gps_csv).readlines())
    p = {}
    indexes = {'timestamp':1, 'lat':2, 'lon':3}
    for d in gps:
        if 'frame' in d:
            indexes['timestamp'] = d.index('timestamp')
            indexes['lat'] = d.index('lat')
            indexes['lon'] = d.index('lon')
        else:
            p[d[0]] = {'timestamp':d[indexes['timestamp']], 'lat':d[indexes['lat']], 'lon':d[indexes['lon']]}


    mylist = []
    for track in root.findall('image'):
        for box in track.findall('box'):
            mydict = box.attrib
            mydict.update(track.attrib)
            mydict.update({'damage':damage_mapping[box.attrib['label']]})
            mydict.update({'video_file':video_file})
            mydict.update(p[track.attrib['id']])

            mylist.append(mydict)
    df = pd.DataFrame(mylist)
    df.xbr = df.xbr.apply(lambda x: str2int(x))
    df.xtl = df.xtl.apply(lambda x: str2int(x))
    df.ybr = df.ybr.apply(lambda x: str2int(x))
    df.ytl = df.ytl.apply(lambda x: str2int(x))
    df.frame = df.id.apply(lambda x: str2int(x))
    df.to_csv(out_path, index=False)

def dump_to_sql(xml_file, gps_csv, video_file):
    user = os.getenv('CRB_SQL_USERNAME')
    password = os.getenv('CRB_SQL_PASSWORD')
    table = os.getenv('CRB_SQL_TABLE')
    csv_file = os.path.join("/mnt/output/", os.path.basename(video_file)[:-4], '.csv')
    print("Generating CSV file to create SQL database...")
    create_csv(xml_file, gps_csv, video_file, csv_file)

    engine = create_engine('mysql+pymysql://{}:{}@mysql.guaminsects.net/videosurvey'.format(user, password))

    df = pd.read_csv(csv_file)
    print("Making connection request to database...")
    conn = engine.connect()
    conn.execute('DROP TABLE IF EXISTS {};'.format(table))
    df.to_sql(table, engine, index=False, if_exists="replace")
    conn.execute('ALTER TABLE {} ADD coords POINT;'.format(table))
    conn.execute('UPDATE {} SET coords=POINT(lon,lat);'.format(table))
    conn.execute('INSERT INTO objects SELECT * FROM {};'.format(table))
    print("Data inserted successfully!")
    conn.close()
