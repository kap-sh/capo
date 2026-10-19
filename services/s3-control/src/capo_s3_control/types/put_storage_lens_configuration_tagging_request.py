"""Generated from Smithy shape ``com.amazonaws.s3control#PutStorageLensConfigurationTaggingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.config_id
    import capo_s3_control.types.storage_lens_tags


class PutStorageLensConfigurationTaggingRequest(TypedDict, closed=True):
    config_id: "capo_s3_control.types.config_id.ConfigId"
    """<p>The ID of the S3 Storage Lens configuration.</p>"""
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The account ID of the requester.</p>"""
    tags: "capo_s3_control.types.storage_lens_tags.StorageLensTags"
    """<p>The tag set of the S3 Storage Lens configuration.</p> <note> <p>You can set up to a maximum of 50 tags.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutStorageLensConfigurationTaggingRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.storage_lens_tags

    capo_s3_control.types.storage_lens_tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> PutStorageLensConfigurationTaggingRequest:
    out: PutStorageLensConfigurationTaggingRequest = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3_control.types.storage_lens_tags

        out["tags"] = capo_s3_control.types.storage_lens_tags.deserialize_xml(
            child_tags
        )
    else:
        out["tags"] = []
    return out
