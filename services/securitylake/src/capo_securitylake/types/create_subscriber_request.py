"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateSubscriberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securitylake.types.access_type_list
    import capo_securitylake.types.aws_identity
    import capo_securitylake.types.description_string
    import capo_securitylake.types.log_source_resource_list
    import capo_securitylake.types.tag_list


class CreateSubscriberRequest(TypedDict, closed=True):
    subscriber_identity: "capo_securitylake.types.aws_identity.AwsIdentity"
    """<p>The Amazon Web Services identity used to access your data.</p>"""
    subscriber_name: "str"
    """<p>The name of your Security Lake subscriber account.</p>"""
    subscriber_description: NotRequired[
        "capo_securitylake.types.description_string.DescriptionString"
    ]
    """<p>The description for your subscriber account in Security Lake.</p>"""
    sources: "capo_securitylake.types.log_source_resource_list.LogSourceResourceList"
    """<p>The supported Amazon Web Services services from which logs and events are collected. Security Lake supports log and event collection for natively supported Amazon Web Services services.</p>"""
    access_types: NotRequired["capo_securitylake.types.access_type_list.AccessTypeList"]
    """<p>The Amazon S3 or Lake Formation access type.</p>"""
    tags: NotRequired["capo_securitylake.types.tag_list.TagList"]
    """<p>An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriberRequest) -> dict:
    out: dict = {}
    import capo_securitylake.types.aws_identity

    out["subscriberIdentity"] = capo_securitylake.types.aws_identity.serialize_json(
        value["subscriber_identity"]
    )
    out["subscriberName"] = value["subscriber_name"]
    if "subscriber_description" in value:
        out["subscriberDescription"] = value["subscriber_description"]
    import capo_securitylake.types.log_source_resource_list

    out["sources"] = capo_securitylake.types.log_source_resource_list.serialize_json(
        value["sources"]
    )
    if "access_types" in value:
        import capo_securitylake.types.access_type_list

        out["accessTypes"] = capo_securitylake.types.access_type_list.serialize_json(
            value["access_types"]
        )
    if "tags" in value:
        import capo_securitylake.types.tag_list

        out["tags"] = capo_securitylake.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSubscriberRequest:
    out: CreateSubscriberRequest = {}  # type: ignore[typeddict-item]
    if data.get("subscriberIdentity") is not None:
        import capo_securitylake.types.aws_identity

        out["subscriber_identity"] = (
            capo_securitylake.types.aws_identity.deserialize_json(
                data["subscriberIdentity"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriberRequest.subscriber_identity required"
        )
    if data.get("subscriberName") is not None:
        out["subscriber_name"] = data["subscriberName"]
    else:
        out["subscriber_name"] = ""
    if data.get("subscriberDescription") is not None:
        out["subscriber_description"] = data["subscriberDescription"]
    if data.get("sources") is not None:
        import capo_securitylake.types.log_source_resource_list

        out["sources"] = (
            capo_securitylake.types.log_source_resource_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        out["sources"] = []
    if data.get("accessTypes") is not None:
        import capo_securitylake.types.access_type_list

        out["access_types"] = capo_securitylake.types.access_type_list.deserialize_json(
            data["accessTypes"]
        )
    if data.get("tags") is not None:
        import capo_securitylake.types.tag_list

        out["tags"] = capo_securitylake.types.tag_list.deserialize_json(data["tags"])
    return out
