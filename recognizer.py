from imageai import Detection

class Recognizer:
    def __init__(self) -> None:
        self.recognizer = Detection.ObjectDetection() #riconosci oggetto
        self.recognizer.setModelTypeAsYOLOv3() #usa yolo per le info
        self.recognizer.setModelPath("yolo.h5") # yolo-tiny.h5 for faster but worse detection (i think)
        self.recognizer.loadModel() #carica tutte i dettagli che ho scritto prima

    #restituisci frame con tag, nome oggetto e probabilità
    def run(self, img):
        img, preds = self.recognizer.detectCustomObjectsFromImage(input_image=img, 
                        custom_objects=None, input_type="array",
                        output_type="array",
                        minimum_percentage_probability=40,
                        display_percentage_probability=True,
                        display_object_name=True)
        return img, preds