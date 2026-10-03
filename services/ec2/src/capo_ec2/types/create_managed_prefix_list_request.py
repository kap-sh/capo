"""Generated from Smithy shape ``com.amazonaws.ec2#CreateManagedPrefixListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.add_prefix_list_entries
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateManagedPrefixListRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    prefix_list_name: NotRequired["capo_ec2.types.string.String"]
    """<p>A name for the prefix list.</p> <p>Constraints: Up to 255 characters in length. The name cannot start with <code>com.amazonaws</code>.</p>"""
    entries: NotRequired["capo_ec2.types.add_prefix_list_entries.AddPrefixListEntries"]
    """<p>One or more entries for the prefix list.</p>"""
    max_entries: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of entries for the prefix list.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the prefix list during creation.</p>"""
    address_family: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address type.</p> <p>Valid Values: <code>IPv4</code> | <code>IPv6</code> </p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p> <p>Constraints: Up to 255 UTF-8 characters in length.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateManagedPrefixListRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "prefix_list_name" in value:
        pairs.append((f"{key_prefix}PrefixListName", str(value["prefix_list_name"])))
    if "entries" in value:
        import capo_ec2.types.add_prefix_list_entries

        capo_ec2.types.add_prefix_list_entries.serialize_ec2_query(
            value["entries"], pairs, f"{key_prefix}Entry"
        )
    if "max_entries" in value:
        pairs.append((f"{key_prefix}MaxEntries", str(value["max_entries"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "address_family" in value:
        pairs.append((f"{key_prefix}AddressFamily", str(value["address_family"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateManagedPrefixListRequest:
    out: CreateManagedPrefixListRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_prefix_list_name = el.find("PrefixListName")
    if child_prefix_list_name is not None:
        out["prefix_list_name"] = str(child_prefix_list_name.text or "")
    child_entries = el.find("Entry")
    if child_entries is not None:
        import capo_ec2.types.add_prefix_list_entries

        out["entries"] = capo_ec2.types.add_prefix_list_entries.deserialize_ec2_query(
            child_entries
        )
    child_max_entries = el.find("MaxEntries")
    if child_max_entries is not None:
        out["max_entries"] = int(child_max_entries.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_address_family = el.find("AddressFamily")
    if child_address_family is not None:
        out["address_family"] = str(child_address_family.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
