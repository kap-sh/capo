"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteDomainEntryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.domain_entry
    import capo_lightsail.types.domain_name


class DeleteDomainEntryRequest(TypedDict, closed=True):
    domain_name: "capo_lightsail.types.domain_name.DomainName"
    """<p>The name of the domain entry to delete.</p>"""
    domain_entry: "capo_lightsail.types.domain_entry.DomainEntry"
    """<p>An array of key-value pairs containing information about your domain entries.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDomainEntryRequest) -> dict:
    out: dict = {}
    out["domainName"] = value["domain_name"]
    import capo_lightsail.types.domain_entry

    out["domainEntry"] = capo_lightsail.types.domain_entry.serialize_aws_json_1_1(
        value["domain_entry"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDomainEntryRequest:
    out: DeleteDomainEntryRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    if data.get("domainEntry") is not None:
        import capo_lightsail.types.domain_entry

        out["domain_entry"] = (
            capo_lightsail.types.domain_entry.deserialize_aws_json_1_1(
                data["domainEntry"]
            )
        )
    else:
        raise DeserializationError("DeleteDomainEntryRequest.domain_entry required")
    return out
