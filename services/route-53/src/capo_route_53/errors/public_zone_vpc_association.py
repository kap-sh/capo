"""Generated from Smithy shape ``com.amazonaws.route53#PublicZoneVPCAssociation``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import ServiceError

if TYPE_CHECKING:
    import capo_route_53.types.error_message


class PublicZoneVPCAssociation_(TypedDict, closed=True):
    message: NotRequired["capo_route_53.types.error_message.ErrorMessage"]
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(value: PublicZoneVPCAssociation_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "message").text = str(value["message"])


def deserialize_xml(el: Element) -> PublicZoneVPCAssociation_:
    out: PublicZoneVPCAssociation_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class PublicZoneVPCAssociation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53#PublicZoneVPCAssociation``."""

    code: str | None = "PublicZoneVPCAssociation"

    def __init__(
        self,
        data: PublicZoneVPCAssociation_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PublicZoneVPCAssociation",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "PublicZoneVPCAssociation":
        return cls(deserialize_xml(el), message, response=response)
