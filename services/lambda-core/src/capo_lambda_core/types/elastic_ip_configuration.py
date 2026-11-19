"""Generated from Smithy shape ``com.amazonaws.lambdacore#ElasticIpConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.elastic_ip_type


class ElasticIpConfiguration(TypedDict, closed=True):
    type: "capo_lambda_core.types.elastic_ip_type.ElasticIpType"
    """The Elastic IP type for the connector's network interfaces."""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticIpConfiguration) -> dict:
    out: dict = {}
    import capo_lambda_core.types.elastic_ip_type

    out["Type"] = capo_lambda_core.types.elastic_ip_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> ElasticIpConfiguration:
    out: ElasticIpConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_lambda_core.types.elastic_ip_type

        out["type"] = capo_lambda_core.types.elastic_ip_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_lambda_core.types.elastic_ip_type.ElasticIpType", ""
        )
    return out
