from pydantic import BaseModel


class ReviewCreate(BaseModel):
    text: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "En mi opinión, no es una como muchos usuarios reclaman. Es un gran paladar que parece ser una parada con muchos grupos de excursión. El menú es más interesante que los otros restaurantes comimos en. La parte más interesante de la experiencia es que el...edificio está en una sección de La Habana Centro. Las plantas inferiores están muy deteriorados, y tienen apartamentos donde viven muchos trabajadores de restaurante. Los pisos superiores, donde el restaurante es, han sido restauradas a gloria pasada. Las reservas son imprescindibles. Plan de 40 a 50 CUC por persona para una comida con cócteles y vinos.Más"
                },
                {
                    "text": "Subiendo las escaleras, puede encontrar un bar en la azotea con unas impresionantes vistas del atardecer. Puedes ver todo el camino hacia el mar, el Capitolio y muchas casas en la ciudad! Es un bonito lugar para pasar horas al atardecer saborea una piña colada...recién preparada (o en una de las muchas otras bebidas)!  El restaurante de la planta baja que necesita para hacer una reserva con antelación, ya que es frecuentemente visitado por muchos turistas. La comida abajo es buena, pero los precios son relativamente altos. En caso de que usted vegetariano: aunque la mayoría de los visitantes son turistas del extranjero, apenas encontrar ningún platos vegetarianos junto a un aperitivo y algunos platos secundarios. El bar de la azotea es sin duda vale la pena visitarlo!Más"
                }
            ]
        }
    }



class ReviewLog(ReviewCreate):
    score: int
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "Llegamos el 17 de febrero, hicimos el check in como en todos los hoteles, para poder entrar a las 15 hrs y resulta que eran pasado de las 17 y aún no terminaban de preparar las habitaciones, y de pilón, el elevador se descompuso ..!!! No lo recomiendo,",
                    "score": 1
                }
            ]
        }
    }

class ReviewResponse(ReviewCreate):
    id: str
    score: int
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "564f7b1d-8f6f-4b3b-8f1d-3f0b7b1d8f6f",
                    "text": "Llegamos el 17 de febrero, hicimos el check in como en todos los hoteles, para poder entrar a las 15 hrs y resulta que eran pasado de las 17 y aún no terminaban de preparar las habitaciones, y de pilón, el elevador se descompuso ..!!! No lo recomiendo,",
                    "score": 1
                }
            ]
        }
    }