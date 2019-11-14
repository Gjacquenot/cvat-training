import sys
import tensorflow as tf
from google.protobuf import text_format
from object_detection.protos import -pipeline_pb2
import argparse

def create_pipeline(pipeline_path,model_path,label_path,train_tfrecord_path,eval_tfrecord_path,out_pipeline_path):
    print((pipeline_path,model_path,label_path,train_tfrecord_path,eval_tfrecord_path,out_pipeline_path))
    pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()                                                                                                                                                                                                          
    with tf.gfile.GFile(pipeline_path, "r") as f:                                                                                                                                                                                                                     
        proto_str = f.read()                                                                                                                                                                                                                                          
        text_format.Merge(proto_str, pipeline_config)                                                                                                                                                                                                                 
    pipeline_config.train_config.fine_tune_checkpoint=model_path
    pipeline_config.train_input_reader.label_map_path=label_path
    pipeline_config.train_input_reader.tf_record_input_reader.input_path[0]=train_tfrecord_path

    pipeline_config.eval_input_reader[0].label_map_path=label_path
    pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[0]=eval_tfrecord_path

    config_text = text_format.MessageToString(pipeline_config)                                                                                                                                                                                                        
    with tf.gfile.Open(out_pipeline_path, "wb") as f:                                                                                                                                                                                                                       
        f.write(config_text)                                                                                                                                                                                                                                       

if __name__== "__main__":


    parser = argparse.ArgumentParser()

    parser.add_argument("-in_pipeline", "--input_pipeline_path", dest = "in_pipeline_path", default = "", help="Model Pipeline Path")
    parser.add_argument("-model", "--input_model_path", dest = "model_path", default = "", help="Input Model Path")
    parser.add_argument("-label", "--label_path",dest ="label_path", help="label_path")
    parser.add_argument("-train_data", "--train_tfrecord_path",dest = "train_tfrecord_path", help="train_tfrecord_path")
    parser.add_argument("-eval_data", "--eval_tfrecord_path",dest = "eval_tfrecord_path", help="eval_tfrecord_path")
    parser.add_argument("-out_pipeline", "--output_pipeline_path", dest = "out_pipeline_path", default = "", help="Output Model Pipeline Path")
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    create_pipeline(args.in_pipeline_path,args.model_path,args.label_path,args.train_tfrecord_path,args.eval_tfrecord_path,args.out_pipeline_path)
