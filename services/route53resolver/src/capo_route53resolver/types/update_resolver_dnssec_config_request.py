"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateResolverDnssecConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.validation


class UpdateResolverDnssecConfigRequest(TypedDict, closed=True):
    resource_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the virtual private cloud (VPC) that you're updating the DNSSEC validation status for.</p>"""
    validation: "capo_route53resolver.types.validation.Validation"
    """<p>The new value that you are specifying for DNSSEC validation for the VPC. The value can be <code>ENABLE</code> or <code>DISABLE</code>. Be aware that it can take time for a validation status change to be completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResolverDnssecConfigRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_route53resolver.types.validation

    out["Validation"] = capo_route53resolver.types.validation.serialize_aws_json_1_1(
        value["validation"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResolverDnssecConfigRequest:
    out: UpdateResolverDnssecConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("Validation") is not None:
        import capo_route53resolver.types.validation

        out["validation"] = (
            capo_route53resolver.types.validation.deserialize_aws_json_1_1(
                data["Validation"]
            )
        )
    else:
        import typing

        out["validation"] = typing.cast(
            "capo_route53resolver.types.validation.Validation", ""
        )
    return out
