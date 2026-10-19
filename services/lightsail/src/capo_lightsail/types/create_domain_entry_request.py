"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateDomainEntryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.domain_entry
    import capo_lightsail.types.domain_name


class CreateDomainEntryRequest(TypedDict, closed=True):
    domain_name: "capo_lightsail.types.domain_name.DomainName"
    """<p>The domain name (<code>example.com</code>) for which you want to create the domain entry.</p>"""
    domain_entry: "capo_lightsail.types.domain_entry.DomainEntry"
    """<p>An array of key-value pairs containing information about the domain entry request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDomainEntryRequest) -> dict:
    out: dict = {}
    out["domainName"] = value["domain_name"]
    import capo_lightsail.types.domain_entry

    out["domainEntry"] = capo_lightsail.types.domain_entry.serialize_aws_json_1_1(
        value["domain_entry"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDomainEntryRequest:
    out: CreateDomainEntryRequest = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("CreateDomainEntryRequest.domain_entry required")
    return out
