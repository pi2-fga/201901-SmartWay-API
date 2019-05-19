from keras.models import load_model
from constants import CROSSWALK, NOT_CROSSWALK
import numpy as np
import cv2 as cv


class CrosswalkCNN(object):
    """
    Classe de redes neurais convolucionais para detecção
    de faixas de pedestre pela visão de um pedestre.
    """

    @classmethod
    def crosswalk_detector(cls, path):
        """
        Ao inserir uma nova image, classifica-la
        como faixa de pedestre ou não faixa de pedestre.

        new_image = Imagem no formato de matriz numpy.

        return classificação das imagens entre ['not_crosswalk', 'crosswalk']
        """

        # Pega a imagem
        img = cls.__img_processing(path)

        __classifier = cls.__get_classifier()

        __prediction = __classifier.predict(img)

        # 0 < prediction < 0.5 = not_crosswalk
        # 0.5 <= prediction < 1 = crosswalk
        print(__prediction)
        is_crosswalk = False
        if float(__prediction) >= 0.5:
            text = CROSSWALK
            is_crosswalk = True
        else:
            text = NOT_CROSSWALK

        print(is_crosswalk, ": " + text)
        return text, is_crosswalk

    @classmethod
    def __img_processing(cls, img):
        """
        Faz todo o processamento da imagem para
        ser usada no algoritmo.
        """

        # Pega a imagem
        new_image = cv.imread(img)

        # Normalizar a imagem (largura=64, altura=64, canais=3)
        new_image = cv.cvtColor(new_image, cv.COLOR_BGR2RGB)
        new_image = cv.resize(new_image, (128, 64), interpolation=cv.INTER_AREA)
        new_image = new_image.astype('float32')
        new_image /= 255

        # Formatar para o formato do tensorFlow (qtd, altura, largura, dimensoes)
        # Verificar se isso não vai dar problema.
        new_image = np.expand_dims(new_image, axis = 0)

        return new_image

    @classmethod
    def __get_classifier(cls):
        """
        Pega o modelo treinado de duas formas
        o modelo com estrutura e os melhores pesos e o modelo
        completo com os melhores pesos armazenados no checkpoint.
        """

        # Podemos também pegar o modelo do checkpoint
        __classifier = load_model('classifiers/crosswalk.hdf5')

        return __classifier
