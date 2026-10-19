"""Generated from Smithy shape ``com.amazonaws.securityir#ImpactedAwsRegion``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.aws_region


class ImpactedAwsRegion(TypedDict, closed=True):
    region: "capo_security_ir.types.aws_region.AwsRegion"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImpactedAwsRegion) -> dict:
    out: dict = {}
    import capo_security_ir.types.aws_region

    out["region"] = capo_security_ir.types.aws_region.serialize_json(value["region"])
    return out


def deserialize_json(data: dict) -> ImpactedAwsRegion:
    out: ImpactedAwsRegion = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        import capo_security_ir.types.aws_region

        out["region"] = capo_security_ir.types.aws_region.deserialize_json(
            data["region"]
        )
    else:
        import typing

        out["region"] = typing.cast("capo_security_ir.types.aws_region.AwsRegion", "")
    return out
