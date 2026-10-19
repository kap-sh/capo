"""Generated from Smithy shape ``com.amazonaws.iam#GenerateServiceLastAccessedDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.access_advisor_usage_granularity_type
    import capo_iam.types.arn_type


class GenerateServiceLastAccessedDetailsRequest(TypedDict, closed=True):
    arn: "capo_iam.types.arn_type.arnType"
    """<p>The ARN of the IAM resource (user, group, role, or managed policy) used to generate information about when the resource was last used in an attempt to access an Amazon Web Services service.</p>"""
    granularity: NotRequired[
        "capo_iam.types.access_advisor_usage_granularity_type.AccessAdvisorUsageGranularityType"
    ]
    """<p>The level of detail that you want to generate. You can specify whether you want to generate information about the last attempt to access services or actions. If you specify service-level granularity, this operation generates only service data. If you specify action-level granularity, it generates service and action data. If you don't include this optional parameter, the operation generates service data.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GenerateServiceLastAccessedDetailsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "granularity" in value:
        import capo_iam.types.access_advisor_usage_granularity_type

        capo_iam.types.access_advisor_usage_granularity_type.serialize_query(
            value["granularity"], pairs, f"{key_prefix}Granularity"
        )


def deserialize_query(el: Element) -> GenerateServiceLastAccessedDetailsRequest:
    out: GenerateServiceLastAccessedDetailsRequest = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        out["arn"] = ""
    child_granularity = el.find("Granularity")
    if child_granularity is not None:
        import capo_iam.types.access_advisor_usage_granularity_type

        out["granularity"] = (
            capo_iam.types.access_advisor_usage_granularity_type.deserialize_query(
                child_granularity
            )
        )
    return out
