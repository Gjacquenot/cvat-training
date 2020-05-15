import os
import sys
from datetime import datetime
time = datetime.now()
stamp = time.strftime("%m%d%Y%H%M%S")
# parse parameters
# sample: epochs=100;num_classes=1
params = {}
for item in sys.argv[1].split(","):
	temp = item.split("=")
	if len(temp) == 2:
		params[temp[0].strip()] = temp[1].strip()

if 'num_clones' not in params:
	params['num_clones'] = 1
	

#TODO: add param for decays


os.system("pip install test-generator")
# os.system("wget https://github.com/opencv/dldt/archive/2018_R5.zip")
# os.system("unzip 2018_R5.zip")
#os.system("git clone https://github.com/tensorflow/models.git /onepanel/extra_repos/tensorflow_models")
os.system("mkdir -p /mnt/src/protoc")
os.system("wget -P /mnt/src/protoc https://github.com/protocolbuffers/protobuf/releases/download/v3.10.1/protoc-3.10.1-linux-x86_64.zip")
os.chdir("/mnt/src/protoc/")
os.system("ls")
os.system("unzip protoc-3.10.1-linux-x86_64.zip")
os.chdir("/mnt/src/tf/research/")
os.system("ls")
#os.system("export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim")
os.system("/mnt/src/protoc/bin/protoc object_detection/protos/*.proto --python_out=.")
os.chdir("/mnt/data/models")
os.system("ls")
os.chdir(params['dataset'])
os.system("ls")
#os.system('latest=$(find . -name "*.tfrecord" -print0 | xargs -r -0 ls -1 -t | head -n1) && unzip -o "$latest"')

if "ssd-mobilenet-v2-coco" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 15000
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/ssd-mobilenet-v2-coco/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/ssd-mobilenet-v2-coco/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))
elif "ssd-mobilenet-v1-coco2" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 15000
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/ssd-mobilenet-v1-coco2/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/ssd-mobilenet-v1-coco2/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))

elif "frcnn-res101-coco" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 10000
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/frcnn-res101-coco/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/frcnn-res101-coco/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))
elif "frcnn-res50-low" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 10000
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/frcnn-res50-lowp/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/frcnn-res50-lowp/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))
elif "frcnn-res50-coco" in params['model'] or "faster-rcnn-res50" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 10000
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /mnt/data/models/pipeline.config -num_classes {} -epochs {} -model /mnt/data/models/model.ckpt -label {}/label_map.pbtxt -train_data {}/default.tfrecord -eval_data {}/default.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))

elif "frcnn-res101-low" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 10
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/frcnn-res101-low/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/frcnn-res101-low/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))
elif "frcnn-nas-coco" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 10
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/frcnn-nas-coco/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/frcnn-nas-coco/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))
elif "frcnn-nas-low" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 10
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/frcnn-nas-low/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/frcnn-nas-low/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))
elif "frcnn-inc-v2-coco" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 10
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/frcnn-inc-v2-coco/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/frcnn-inc-v2-coco/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))
elif "frcnn-inc-resv2-atr-coco" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 10
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/frcnn-inc-resv2-atr-coco/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/frcnn-inc-resv2-atr-coco/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))
elif "faster-rcnn-inception-resnet-atrous-oid" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 10
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/faster-rcnn-inception-resnet-atrous-oid/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/faster-rcnn-inception-resnet-atrous-oid/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))
elif "ssdlite-mobilenet-coco" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 10
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/ssdlite-mobilenet-coco/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/ssdlite-mobilenet-coco/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))
elif "ssd-mobilenet-v1-quantized-coco" in params['model']:
	if 'epochs' not in params:
		params['epochs'] = 10
	os.system("python /mnt/src/train/create_pipeline_v2.py -in_pipeline /onepanel/input/datasets/onepanel-demo/ssd-mobilenet-v1-quantized-coco/1/pipeline.config -num_classes {} -epochs {} -model /onepanel/input/datasets/onepanel-demo/ssd-mobilenet-v1-quantized-coco/1/model.ckpt -label {}/label_map.pbtxt -train_data {}/training.tfrecord -eval_data {}/training.tfrecord -out_pipeline /mnt/output/pipeline.config -num_clones {}".format(params["num_classes"], params["epochs"], params["dataset"], params["dataset"], params["dataset"], params["num_clones"]))

temp = os.getcwd()
os.chdir("/mnt/output")
os.system("ls")
os.chdir(temp)



os.system("python /mnt/src/tf/research/object_detection/legacy/train.py --train_dir=/mnt/output/ --pipeline_config_path=/mnt/output/pipeline.config --num_clones={}".format(params['num_clones']))
os.system("python /mnt/src/tf/research/object_detection/export_inference_graph.py --input-type=image_tensor --pipeline_config_path=/mnt/output/pipeline.config --trained_checkpoint_prefix=/mnt/output/model.ckpt-{} --output_directory=/mnt/output".format(params["epochs"]))


#generate lable map
os.system("python /mnt/src/train/convert_json_workflow.py {}/".format(params['dataset']))
dataset_name = "{}-model-output-{}".format(params['model'], stamp)
os.system("onepanel datasets create {}".format(dataset_name))
os.chdir("{}".format(dataset_name))
# os.mkdir("tf_annotation_model")
os.system("mv /mnt/output/frozen_inference_graph.pb {}/".format(dataset_name))
os.system("mv /mnt/output/classes.csv {}/".format(dataset_name))
os.system("ls")
# os.system("mv /mnt/src/dldt-2018_R5/model-optimizer/{}/tf_annotation_model/frozen_inference_graph.pb /mnt/src/dldt-2018_R5/model-optimizer/{}/tf_annotation_model/{}_frozen_inference_graph.pb".format(dataset_name, dataset_name, params['model']))
# os.system("mv /mnt/src/dldt-2018_R5/model-optimizer/frozen_inference_graph.bin /mnt/src/dldt-2018_R5/model-optimizer/{}/".format(dataset_name))
# os.system("mv /mnt/src/dldt-2018_R5/model-optimizer/frozen_inference_graph.xml /mnt/src/dldt-2018_R5/model-optimizer/{}/".format(dataset_name))
# if "ssd" in params['model']:
# 	os.system("mv /mnt/src/train/interp_scripts/ssd_interp.py /mnt/src/dldt-2018_R5/model-optimizer/{}/".format(dataset_name))
# 	os.system("mv /mnt/src/dldt-2018_R5/model-optimizer/{}/ssd_interp.py /mnt/src/dldt-2018_R5/model-optimizer/{}/interp.py".format(dataset_name, dataset_name))

# elif "faster" in params['model'] or "frcnn" in params['model']:
# 	os.system("mv /mnt/src/train/interp_scripts/faster_interp.py /mnt/src/dldt-2018_R5/model-optimizer/{}/".format(dataset_name))
# 	os.system("mv /mnt/src/dldt-2018_R5/model-optimizer/{}/faster_interp.py /mnt/src/dldt-2018_R5/model-optimizer/{}/interp.py".format(dataset_name, dataset_name))

# os.system("mv /mnt/output/label_map.json /mnt/src/dldt-2018_R5/model-optimizer/{}/".format(dataset_name))
# os.chdir("/onepanel/code/dldt-2018_R5/model-optimizer{}".format(dataset_name))
os.system('onepanel datasets push -m "update" --source job')
print("\n\n")
print("*******************************************************************************")
print("Dataset with Trained Model: ", dataset_name)
#
