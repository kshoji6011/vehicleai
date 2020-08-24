import coremltools

coreml_model = coremltools.converters.keras.convert(
    'vehicle_cnn_aug.h5',
    input_names='image',
    image_input_names='image',
    output_names='Prediction',
    class_labels=['car', 'bycycle', 'motorcycle', 'pedestrian'],
)

coreml_model.save('./vehicle_cnn_aug.mlmodel')