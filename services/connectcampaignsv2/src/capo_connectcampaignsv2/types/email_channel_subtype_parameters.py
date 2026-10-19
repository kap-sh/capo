"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#EmailChannelSubtypeParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.attributes
    import capo_connectcampaignsv2.types.email_address


class EmailChannelSubtypeParameters(TypedDict, closed=True):
    destination_email_address: (
        "capo_connectcampaignsv2.types.email_address.EmailAddress"
    )
    connect_source_email_address: NotRequired[
        "capo_connectcampaignsv2.types.email_address.EmailAddress"
    ]
    template_arn: NotRequired["capo_connectcampaignsv2.types.arn.Arn"]
    template_parameters: "capo_connectcampaignsv2.types.attributes.Attributes"


# --- restJson1 ser/de ---
def serialize_json(value: EmailChannelSubtypeParameters) -> dict:
    out: dict = {}
    out["destinationEmailAddress"] = value["destination_email_address"]
    if "connect_source_email_address" in value:
        out["connectSourceEmailAddress"] = value["connect_source_email_address"]
    if "template_arn" in value:
        out["templateArn"] = value["template_arn"]
    import capo_connectcampaignsv2.types.attributes

    out["templateParameters"] = capo_connectcampaignsv2.types.attributes.serialize_json(
        value["template_parameters"]
    )
    return out


def deserialize_json(data: dict) -> EmailChannelSubtypeParameters:
    out: EmailChannelSubtypeParameters = {}  # type: ignore[typeddict-item]
    if data.get("destinationEmailAddress") is not None:
        out["destination_email_address"] = data["destinationEmailAddress"]
    else:
        out["destination_email_address"] = ""
    if data.get("connectSourceEmailAddress") is not None:
        out["connect_source_email_address"] = data["connectSourceEmailAddress"]
    if data.get("templateArn") is not None:
        out["template_arn"] = data["templateArn"]
    if data.get("templateParameters") is not None:
        import capo_connectcampaignsv2.types.attributes

        out["template_parameters"] = (
            capo_connectcampaignsv2.types.attributes.deserialize_json(
                data["templateParameters"]
            )
        )
    else:
        out["template_parameters"] = {}
    return out


def redact_sensitive(value: EmailChannelSubtypeParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "destination_email_address" in value:
        out["destination_email_address"] = "*** Sensitive Data Redacted ***"
    if "connect_source_email_address" in value:
        out["connect_source_email_address"] = "*** Sensitive Data Redacted ***"
    if "template_parameters" in value:
        out["template_parameters"] = "*** Sensitive Data Redacted ***"
    return out
