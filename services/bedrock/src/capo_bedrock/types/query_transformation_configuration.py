"""Generated from Smithy shape ``com.amazonaws.bedrock#QueryTransformationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.query_transformation_type


class QueryTransformationConfiguration(TypedDict, closed=True):
    type: "capo_bedrock.types.query_transformation_type.QueryTransformationType"
    """<p>The type of transformation to apply to the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryTransformationConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock.types.query_transformation_type

    out["type"] = capo_bedrock.types.query_transformation_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> QueryTransformationConfiguration:
    out: QueryTransformationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock.types.query_transformation_type

        out["type"] = capo_bedrock.types.query_transformation_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock.types.query_transformation_type.QueryTransformationType", ""
        )
    return out
