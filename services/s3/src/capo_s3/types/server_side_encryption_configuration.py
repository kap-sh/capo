"""Generated from Smithy shape ``com.amazonaws.s3#ServerSideEncryptionConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.server_side_encryption_rules


class ServerSideEncryptionConfiguration(TypedDict, closed=True):
    rules: "capo_s3.types.server_side_encryption_rules.ServerSideEncryptionRules"
    """<p>Container for information about a particular server-side encryption configuration rule.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ServerSideEncryptionConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.server_side_encryption_rules

    capo_s3.types.server_side_encryption_rules.serialize_xml_flat(
        value["rules"], el, "Rule"
    )


def deserialize_xml(el: Element) -> ServerSideEncryptionConfiguration:
    out: ServerSideEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if el.find("Rule") is not None:
        import capo_s3.types.server_side_encryption_rules

        out["rules"] = capo_s3.types.server_side_encryption_rules.deserialize_xml_flat(
            el, "Rule"
        )
    else:
        raise DeserializationError("ServerSideEncryptionConfiguration.rules required")
    return out


def redact_sensitive(value: ServerSideEncryptionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rules" in value:
        import capo_s3.types.server_side_encryption_rules

        out["rules"] = capo_s3.types.server_side_encryption_rules.redact_sensitive(
            value["rules"]
        )
    return out
