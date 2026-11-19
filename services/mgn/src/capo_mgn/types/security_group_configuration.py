"""Generated from Smithy shape ``com.amazonaws.mgn#SecurityGroupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.security_group_associations


class SecurityGroupConfiguration(TypedDict, closed=True):
    associations: NotRequired[
        "capo_mgn.types.security_group_associations.SecurityGroupAssociations"
    ]
    """<p>The CIDR ranges and machine identifiers that associate source machines with the security group. Each list provided replaces the stored list rather than merging into it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupConfiguration) -> dict:
    out: dict = {}
    if "associations" in value:
        import capo_mgn.types.security_group_associations

        out["associations"] = capo_mgn.types.security_group_associations.serialize_json(
            value["associations"]
        )
    return out


def deserialize_json(data: dict) -> SecurityGroupConfiguration:
    out: SecurityGroupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("associations") is not None:
        import capo_mgn.types.security_group_associations

        out["associations"] = (
            capo_mgn.types.security_group_associations.deserialize_json(
                data["associations"]
            )
        )
    return out
