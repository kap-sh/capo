"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#Vpc``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__list_of__string


class Vpc(TypedDict, closed=True):
    security_groups: NotRequired[
        "capo_kafkaconnect.types.__list_of__string.__listOf__string"
    ]
    """<p>The security groups for the connector.</p>"""
    subnets: "capo_kafkaconnect.types.__list_of__string.__listOf__string"
    """<p>The subnets for the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Vpc) -> dict:
    out: dict = {}
    if "security_groups" in value:
        import capo_kafkaconnect.types.__list_of__string

        out["securityGroups"] = (
            capo_kafkaconnect.types.__list_of__string.serialize_json(
                value["security_groups"]
            )
        )
    import capo_kafkaconnect.types.__list_of__string

    out["subnets"] = capo_kafkaconnect.types.__list_of__string.serialize_json(
        value["subnets"]
    )
    return out


def deserialize_json(data: dict) -> Vpc:
    out: Vpc = {}  # type: ignore[typeddict-item]
    if data.get("securityGroups") is not None:
        import capo_kafkaconnect.types.__list_of__string

        out["security_groups"] = (
            capo_kafkaconnect.types.__list_of__string.deserialize_json(
                data["securityGroups"]
            )
        )
    if data.get("subnets") is not None:
        import capo_kafkaconnect.types.__list_of__string

        out["subnets"] = capo_kafkaconnect.types.__list_of__string.deserialize_json(
            data["subnets"]
        )
    else:
        out["subnets"] = []
    return out
