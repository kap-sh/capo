"""Generated from Smithy shape ``com.amazonaws.route53#ProtectionAlreadyExists``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import ServiceError

if TYPE_CHECKING:
    import capo_route_53.types.error_message
    import capo_route_53.types.protection_errors


class ProtectionAlreadyExists_(TypedDict, closed=True):
    message: NotRequired["capo_route_53.types.error_message.ErrorMessage"]
    """<p>A message that explains that a protection already exists for every name and type in the <code>CreateResourceRecordSetProtections</code> request.</p>"""
    errors: "capo_route_53.types.protection_errors.ProtectionErrors"
    """<p>The entries that already have a protection.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ProtectionAlreadyExists_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])
    import capo_route_53.types.protection_errors

    capo_route_53.types.protection_errors.serialize_xml(value["errors"], el, "Errors")


def deserialize_xml(el: Element) -> ProtectionAlreadyExists_:
    out: ProtectionAlreadyExists_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_errors = el.find("Errors")
    if child_errors is not None:
        import capo_route_53.types.protection_errors

        out["errors"] = capo_route_53.types.protection_errors.deserialize_xml(
            child_errors
        )
    else:
        out["errors"] = []
    return out


class ProtectionAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53#ProtectionAlreadyExists``."""

    code: str | None = "ProtectionAlreadyExists"

    def __init__(
        self,
        data: ProtectionAlreadyExists_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ProtectionAlreadyExists",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ProtectionAlreadyExists":
        return cls(deserialize_xml(el), message, response=response)
