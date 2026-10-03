"""Generated from Smithy shape ``com.amazonaws.securitylake#UpdateSubscriberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.aws_identity
    import capo_securitylake.types.description_string
    import capo_securitylake.types.log_source_resource_list
    import capo_securitylake.types.safe_string
    import capo_securitylake.types.uuid


class UpdateSubscriberRequest(TypedDict, closed=True):
    subscriber_id: "capo_securitylake.types.uuid.UUID"
    """<p>A value created by Security Lake that uniquely identifies your subscription.</p>"""
    subscriber_identity: NotRequired["capo_securitylake.types.aws_identity.AwsIdentity"]
    """<p>The Amazon Web Services identity used to access your data.</p>"""
    subscriber_name: NotRequired["capo_securitylake.types.safe_string.SafeString"]
    """<p>The name of the Security Lake account subscriber.</p>"""
    subscriber_description: NotRequired[
        "capo_securitylake.types.description_string.DescriptionString"
    ]
    """<p>The description of the Security Lake account subscriber.</p>"""
    sources: NotRequired[
        "capo_securitylake.types.log_source_resource_list.LogSourceResourceList"
    ]
    """<p>The supported Amazon Web Services services from which logs and events are collected. For the list of supported Amazon Web Services services, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html">Amazon Security Lake User Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriberRequest) -> dict:
    out: dict = {}
    if "subscriber_identity" in value:
        import capo_securitylake.types.aws_identity

        out["subscriberIdentity"] = capo_securitylake.types.aws_identity.serialize_json(
            value["subscriber_identity"]
        )
    if "subscriber_name" in value:
        out["subscriberName"] = value["subscriber_name"]
    if "subscriber_description" in value:
        out["subscriberDescription"] = value["subscriber_description"]
    if "sources" in value:
        import capo_securitylake.types.log_source_resource_list

        out["sources"] = (
            capo_securitylake.types.log_source_resource_list.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSubscriberRequest:
    out: UpdateSubscriberRequest = {}  # type: ignore[typeddict-item]
    if data.get("subscriberIdentity") is not None:
        import capo_securitylake.types.aws_identity

        out["subscriber_identity"] = (
            capo_securitylake.types.aws_identity.deserialize_json(
                data["subscriberIdentity"]
            )
        )
    if data.get("subscriberName") is not None:
        out["subscriber_name"] = data["subscriberName"]
    if data.get("subscriberDescription") is not None:
        out["subscriber_description"] = data["subscriberDescription"]
    if data.get("sources") is not None:
        import capo_securitylake.types.log_source_resource_list

        out["sources"] = (
            capo_securitylake.types.log_source_resource_list.deserialize_json(
                data["sources"]
            )
        )
    return out
