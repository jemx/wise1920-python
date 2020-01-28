import tensorflow as tf
import tensorflow_datasets as tfds

iris = tfds.load("iris", split="train", as_supervised=True).shuffle(4096)
           .batch(10)

iris_validation = iris.take(5)
iris_train = iris.skip(5)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(3, activation="softmax")
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(iris_train, epochs=70, validation_data=iris_validation, 
          validation_steps=5)