"""Generated from Smithy shape ``com.amazonaws.s3vectors#QueryVectorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.distance_metric
    import capo_s3vectors.types.query_vectors_next_token
    import capo_s3vectors.types.query_vectors_output_list


class QueryVectorsOutput(TypedDict, closed=True):
    vectors: "capo_s3vectors.types.query_vectors_output_list.QueryVectorsOutputList"
    """<p>The vectors in the approximate nearest neighbor search.</p>"""
    distance_metric: NotRequired["capo_s3vectors.types.distance_metric.DistanceMetric"]
    """<p>The distance metric that was used for the similarity search calculation. This is the same distance metric that was configured for the vector index when it was created.</p>"""
    next_token: NotRequired[
        "capo_s3vectors.types.query_vectors_next_token.QueryVectorsNextToken"
    ]
    """<p>Pagination token to be used in the subsequent page request. The field is empty if no further pagination is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryVectorsOutput) -> dict:
    out: dict = {}
    import capo_s3vectors.types.query_vectors_output_list

    out["vectors"] = capo_s3vectors.types.query_vectors_output_list.serialize_json(
        value["vectors"]
    )
    if "distance_metric" in value:
        import capo_s3vectors.types.distance_metric

        out["distanceMetric"] = capo_s3vectors.types.distance_metric.serialize_json(
            value["distance_metric"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> QueryVectorsOutput:
    out: QueryVectorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("vectors") is not None:
        import capo_s3vectors.types.query_vectors_output_list

        out["vectors"] = (
            capo_s3vectors.types.query_vectors_output_list.deserialize_json(
                data["vectors"]
            )
        )
    else:
        out["vectors"] = []
    if data.get("distanceMetric") is not None:
        import capo_s3vectors.types.distance_metric

        out["distance_metric"] = capo_s3vectors.types.distance_metric.deserialize_json(
            data["distanceMetric"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
