import tensorflow as tf
import tensorflow_datasets as tfds

def transform_images(image, label):
    image = tf.image.resize(image, (64, 64))
    image = image / 255
    return image, label

catsdogs = tfds.load("cats_vs_dogs", split="train", as_supervised=True).map(transform_images)
catsdogs_validation = catsdogs.take(64).batch(64)
catsdogs_train = catsdogs.skip(64).batch(64).repeat()

mnet = tf.keras.applications.mobilenet_v2.MobileNetV2(
          input_shape=(160, 160, 3), include_top=False, weights='imagenet'
        )
mnet.trainable = False
mnet.summary()
model = tf.keras.models.Sequential([
        mnet,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dropout(0.4),
        tf.keras.layers.Dense(2, activation="softmax"),
])
model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(catsdogs_train, epochs=5, steps_per_epoch=32, validation_data=catsdogs_validation,validation_steps=1)
