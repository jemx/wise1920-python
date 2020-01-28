import tensorflow as tf
import tensorflow_datasets as tfds

mnist = tfds.load("mnist", as_supervised=True)
mnist_train = mnist["train"].take(4096).shuffle(4096).batch(128).repeat()
mnist_validation = mnist["test"].take(128).batch(32)

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(mnist_train, epochs=40, steps_per_epoch=32, 
          validation_data=mnist_validation, validation_steps=4)

