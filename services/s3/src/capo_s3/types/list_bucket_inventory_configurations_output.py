"""Generated from Smithy shape ``com.amazonaws.s3#ListBucketInventoryConfigurationsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.inventory_configuration_list
    import capo_s3.types.is_truncated
    import capo_s3.types.next_token
    import capo_s3.types.token


class ListBucketInventoryConfigurationsOutput(TypedDict, closed=True):
    continuation_token: NotRequired["capo_s3.types.token.Token"]
    """<p>If sent in the request, the marker that is used as a starting point for this inventory configuration list response.</p>"""
    inventory_configuration_list: NotRequired[
        "capo_s3.types.inventory_configuration_list.InventoryConfigurationList"
    ]
    """<p>The list of inventory configurations for a bucket.</p>"""
    is_truncated: NotRequired["capo_s3.types.is_truncated.IsTruncated"]
    """<p>Tells whether the returned list of inventory configurations is complete. A value of true indicates that the list is not complete and the NextContinuationToken is provided for a subsequent request.</p>"""
    next_continuation_token: NotRequired["capo_s3.types.next_token.NextToken"]
    """<p>The marker used to continue this inventory configuration listing. Use the <code>NextContinuationToken</code> from this response to continue the listing in a subsequent request. The continuation token is an opaque value that Amazon S3 understands.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListBucketInventoryConfigurationsOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "continuation_token" in value:
        SubElement(el, "ContinuationToken").text = str(value["continuation_token"])
    if "inventory_configuration_list" in value:
        import capo_s3.types.inventory_configuration_list

        capo_s3.types.inventory_configuration_list.serialize_xml_flat(
            value["inventory_configuration_list"], el, "InventoryConfiguration"
        )
    if "is_truncated" in value:
        SubElement(el, "IsTruncated").text = (
            "true" if value["is_truncated"] else "false"
        )
    if "next_continuation_token" in value:
        SubElement(el, "NextContinuationToken").text = str(
            value["next_continuation_token"]
        )


def deserialize_xml(el: Element) -> ListBucketInventoryConfigurationsOutput:
    out: ListBucketInventoryConfigurationsOutput = {}  # type: ignore[typeddict-item]
    child_continuation_token = el.find("ContinuationToken")
    if child_continuation_token is not None:
        out["continuation_token"] = str(child_continuation_token.text or "")
    if el.find("InventoryConfiguration") is not None:
        import capo_s3.types.inventory_configuration_list

        out["inventory_configuration_list"] = (
            capo_s3.types.inventory_configuration_list.deserialize_xml_flat(
                el, "InventoryConfiguration"
            )
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    child_next_continuation_token = el.find("NextContinuationToken")
    if child_next_continuation_token is not None:
        out["next_continuation_token"] = str(child_next_continuation_token.text or "")
    return out


def redact_sensitive(value: ListBucketInventoryConfigurationsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inventory_configuration_list" in value:
        import capo_s3.types.inventory_configuration_list

        out["inventory_configuration_list"] = (
            capo_s3.types.inventory_configuration_list.redact_sensitive(
                value["inventory_configuration_list"]
            )
        )
    return out
