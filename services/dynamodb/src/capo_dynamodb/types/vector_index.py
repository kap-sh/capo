"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.positive_long_object
    import capo_dynamodb.types.projection
    import capo_dynamodb.types.search_schema
    import capo_dynamodb.types.vector_attribute_definition
    import capo_dynamodb.types.vector_distance_function


class VectorIndex(TypedDict, closed=True):
    index_name: "capo_dynamodb.types.index_name.IndexName"
    """<p>The name of the vector index.</p>"""
    vector_attribute: (
        "capo_dynamodb.types.vector_attribute_definition.VectorAttributeDefinition"
    )
    """<p>The vector attribute configuration for the index.</p>"""
    search_schema: NotRequired["capo_dynamodb.types.search_schema.SearchSchema"]
    """<p>The search schema that defines partition key and inline filter attributes for the vector index.</p>"""
    projection: "capo_dynamodb.types.projection.Projection"
    """<p>Specifies attributes that are copied (projected) from the table into the vector index.</p>"""
    dimensions: "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    """<p>The number of dimensions in each vector.</p>"""
    distance_function: (
        "capo_dynamodb.types.vector_distance_function.VectorDistanceFunction"
    )
    """<p>The distance function used to calculate similarity between vectors. Valid values: <code>COSINE</code>, <code>EUCLIDEAN</code>, <code>DOT_PRODUCT</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VectorIndex) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    import capo_dynamodb.types.vector_attribute_definition

    out["VectorAttribute"] = (
        capo_dynamodb.types.vector_attribute_definition.serialize_aws_json_1_0(
            value["vector_attribute"]
        )
    )
    if "search_schema" in value:
        import capo_dynamodb.types.search_schema

        out["SearchSchema"] = capo_dynamodb.types.search_schema.serialize_aws_json_1_0(
            value["search_schema"]
        )
    import capo_dynamodb.types.projection

    out["Projection"] = capo_dynamodb.types.projection.serialize_aws_json_1_0(
        value["projection"]
    )
    out["Dimensions"] = value["dimensions"]
    import capo_dynamodb.types.vector_distance_function

    out["DistanceFunction"] = (
        capo_dynamodb.types.vector_distance_function.serialize_aws_json_1_0(
            value["distance_function"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> VectorIndex:
    out: VectorIndex = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        out["index_name"] = ""
    if data.get("VectorAttribute") is not None:
        import capo_dynamodb.types.vector_attribute_definition

        out["vector_attribute"] = (
            capo_dynamodb.types.vector_attribute_definition.deserialize_aws_json_1_0(
                data["VectorAttribute"]
            )
        )
    else:
        raise DeserializationError("VectorIndex.vector_attribute required")
    if data.get("SearchSchema") is not None:
        import capo_dynamodb.types.search_schema

        out["search_schema"] = (
            capo_dynamodb.types.search_schema.deserialize_aws_json_1_0(
                data["SearchSchema"]
            )
        )
    if data.get("Projection") is not None:
        import capo_dynamodb.types.projection

        out["projection"] = capo_dynamodb.types.projection.deserialize_aws_json_1_0(
            data["Projection"]
        )
    else:
        raise DeserializationError("VectorIndex.projection required")
    if data.get("Dimensions") is not None:
        out["dimensions"] = data["Dimensions"]
    else:
        out["dimensions"] = 0
    if data.get("DistanceFunction") is not None:
        import capo_dynamodb.types.vector_distance_function

        out["distance_function"] = (
            capo_dynamodb.types.vector_distance_function.deserialize_aws_json_1_0(
                data["DistanceFunction"]
            )
        )
    else:
        import typing

        out["distance_function"] = typing.cast(
            "capo_dynamodb.types.vector_distance_function.VectorDistanceFunction", ""
        )
    return out
