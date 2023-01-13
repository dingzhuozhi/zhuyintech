from tensorflow import keras


class speech_model:
    # 训练参数
    lr = 1e-4
    epoch = 500
    batch_size = 32

    # 网络参数
    dim_input = 25
    units = 16
    num_class = 3
    timesteps = 30

    # 模型
    model = None

    def __init__(self, max_len, mode):
        self.timesteps = max_len
        model = keras.Sequential()
        model.add(keras.layers.BatchNormalization(input_shape=(self.timesteps, self.dim_input)))
        model.add(keras.layers.Bidirectional(
            keras.layers.LSTM(self.units, return_sequences=True)))
        model.add(keras.layers.Bidirectional(
            keras.layers.GRU(self.units)))
        # model.add(keras.layers.Average())
        model.add(keras.layers.Dense(128, activation='relu'))
        model.add(keras.layers.BatchNormalization())
        model.add(keras.layers.Dense(self.num_class, activation='softmax'))
        self.model = model
        if mode == 'test':
            self.model.load_weights("./best_model_weight/best_weights.hdf5")

    def train(self, trainx, trainy, testx, testy):
        best_weights_filepath = './best_model_weight/best_weights.hdf5'
        earlyStopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, verbose=1, mode='min')
        saveBestModel = keras.callbacks.ModelCheckpoint(best_weights_filepath, monitor='val_acc', verbose=1,
                                                        save_best_only=True, mode='max', period=10)
        self.model.compile(optimizer=keras.optimizers.Adam(self.lr), loss=keras.losses.categorical_crossentropy,
                           metrics=['accuracy'])
        self.model.fit(trainx, trainy, epochs=self.epoch, batch_size=self.batch_size, validation_data=(testx, testy),
                       callbacks=[earlyStopping, saveBestModel])

    def test(self, data):
        return self.model.predict(data, batch_size=1)


