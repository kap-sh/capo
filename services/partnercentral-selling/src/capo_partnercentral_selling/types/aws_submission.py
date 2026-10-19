"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsSubmission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.sales_involvement_type
    import capo_partnercentral_selling.types.visibility


class AwsSubmission(TypedDict, closed=True):
    involvement_type: (
        "capo_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType"
    )
    """<p>Specifies the type of AWS involvement in the opportunity, such as coselling, deal support, or technical consultation. This helps categorize the nature of AWS participation.</p>"""
    visibility: NotRequired["capo_partnercentral_selling.types.visibility.Visibility"]
    """<p>Determines who can view AWS involvement in the opportunity. Typically, this field is set to <code>Full</code> for most cases, but it may be restricted based on special program requirements or confidentiality needs.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsSubmission) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.sales_involvement_type

    out["InvolvementType"] = (
        capo_partnercentral_selling.types.sales_involvement_type.serialize_aws_json_1_0(
            value["involvement_type"]
        )
    )
    if "visibility" in value:
        import capo_partnercentral_selling.types.visibility

        out["Visibility"] = (
            capo_partnercentral_selling.types.visibility.serialize_aws_json_1_0(
                value["visibility"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsSubmission:
    out: AwsSubmission = {}  # type: ignore[typeddict-item]
    if data.get("InvolvementType") is not None:
        import capo_partnercentral_selling.types.sales_involvement_type

        out["involvement_type"] = (
            capo_partnercentral_selling.types.sales_involvement_type.deserialize_aws_json_1_0(
                data["InvolvementType"]
            )
        )
    else:
        import typing

        out["involvement_type"] = typing.cast(
            "capo_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType",
            "",
        )
    if data.get("Visibility") is not None:
        import capo_partnercentral_selling.types.visibility

        out["visibility"] = (
            capo_partnercentral_selling.types.visibility.deserialize_aws_json_1_0(
                data["Visibility"]
            )
        )
    return out
