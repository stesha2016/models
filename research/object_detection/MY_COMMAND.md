# My notebook

# Build protoc
[Download protoc](https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip),unzip to protoc folder, and set protoc folder under research folder.
```
./protoc/bin/protoc object_detection/protos/*.proto --python_out=.
```
```
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
```
```
python object_detection/builders/model_builder_test.py
```
test on tenserflow 1.9.0

# =========================================================================== #
# xml to csv
# =========================================================================== #
modify PROJECT info
```
python xml_to_csv.py
```

# =========================================================================== #
# csv to tfrecord
# =========================================================================== #
```
python generate_tfrecord.py --dataset=boxes
```

# =========================================================================== #
# training project
# =========================================================================== #
```
python model_main.py --logtostderr \
                     --model_dir=project_images/boxes/logs \
                     --pipeline_config_path=project_images/boxes/config/ssd_mobilenet_v2.config
```
or
```
python legacy/train.py --logtostderr \
                     --train_dir=project_images/boxes/logs \
                     --pipeline_config_path=project_images/boxes/config/ssd_mobilenet_v2.config
```

# =========================================================================== #
# convert ckpt to pb
# =========================================================================== #
under research folder
```
python object_detection/export_inference_graph.py \
                        --input_type image_tensor \
                        --pipeline_config_path object_detection/project_images/boxes/config/ssd_mobilenet_v2.config \
                        --trained_checkpoint_prefix object_detection/project_images/boxes/logs/model.ckpt-7386 \
                        --output_directory object_detection/project_images/boxes/logs/saved_model
```

# =========================================================================== #
# convert ckpt to tflite pb
# =========================================================================== #
```
python object_detection/export_tflite_ssd_graph.py \
				--pipeline_config_path=object_detection/project_images/boxes/config/ssd_mobilenet_v2.config \
				--trained_checkpoint_prefix=object_detection/project_images/boxes/logs/model.ckpt-7386 \
				--output_directory=object_detection/project_images/boxes/logs/tflite \
				--add_postprocessing_op=true
```

# =========================================================================== #
# build toco tool
# =========================================================================== #
```
bazel build tensorflow/python/tools:freeze_graph
bazel build tensorflow/lite/toco:toco
```

# =========================================================================== #
# convert pb to tflite
# =========================================================================== #
```
bazel run tensorflow/lite/toco:toco -- --input_file=/local/deeplearning/models/research/object_detection/project_images/boxes/logs/tflite/tflite_graph.pb --output_file=/local/deeplearning/models/research/object_detection/project_images/boxes/logs/tflite/ssd_mobilenetv2.tflite --input_shapes=1,300,300,3 --input_arrays=normalized_input_image_tensor --output_arrays='TFLite_Detection_PostProcess','TFLite_Detection_PostProcess:1','TFLite_Detection_PostProcess:2','TFLite_Detection_PostProcess:3' --inference_type=FLOAT --allow_custom_ops
```