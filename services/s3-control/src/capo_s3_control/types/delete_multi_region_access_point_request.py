"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteMultiRegionAccessPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.delete_multi_region_access_point_input
    import capo_s3_control.types.multi_region_access_point_client_token


class DeleteMultiRegionAccessPointRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>"""
    client_token: "capo_s3_control.types.multi_region_access_point_client_token.MultiRegionAccessPointClientToken"
    """<p>An idempotency token used to identify the request and guarantee that requests are unique.</p>"""
    details: "capo_s3_control.types.delete_multi_region_access_point_input.DeleteMultiRegionAccessPointInput"
    """<p>A container element containing details about the Multi-Region Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteMultiRegionAccessPointRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "ClientToken").text = str(value["client_token"])
    import capo_s3_control.types.delete_multi_region_access_point_input

    capo_s3_control.types.delete_multi_region_access_point_input.serialize_xml(
        value["details"], el, "Details"
    )


def deserialize_xml(el: Element) -> DeleteMultiRegionAccessPointRequest:
    out: DeleteMultiRegionAccessPointRequest = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    else:
        out["client_token"] = ""
    child_details = el.find("Details")
    if child_details is not None:
        import capo_s3_control.types.delete_multi_region_access_point_input

        out["details"] = (
            capo_s3_control.types.delete_multi_region_access_point_input.deserialize_xml(
                child_details
            )
        )
    else:
        raise DeserializationError(
            "DeleteMultiRegionAccessPointRequest.details required"
        )
    return out
