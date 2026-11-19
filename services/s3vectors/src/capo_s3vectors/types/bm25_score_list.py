"""Generated from Smithy shape ``com.amazonaws.s3vectors#Bm25ScoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3vectors.types.bm25_score

Bm25ScoreList: TypeAlias = list["capo_s3vectors.types.bm25_score.Bm25Score"]


# --- restJson1 ser/de ---
def serialize_json(value: Bm25ScoreList) -> list:
    import capo_s3vectors.types.bm25_score

    out: list = []
    for item in value:
        out.append(capo_s3vectors.types.bm25_score.serialize_json(item))
    return out


def deserialize_json(data: list) -> Bm25ScoreList:
    import capo_s3vectors.types.bm25_score

    out: Bm25ScoreList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_s3vectors.types.bm25_score.deserialize_json(item))
    return out
