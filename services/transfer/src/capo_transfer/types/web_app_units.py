"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppUnits``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, SerializationError
from capo_transfer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_transfer.types.web_app_unit_count


class WebAppUnitsProvisionedMember(TypedDict, closed=True):
    Provisioned: "capo_transfer.types.web_app_unit_count.WebAppUnitCount"


WebAppUnits: TypeAlias = WebAppUnitsProvisionedMember | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAppUnits) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"WebAppUnits: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Provisioned" in value:
        return {"Provisioned": value["Provisioned"]}
    else:
        raise SerializationError("WebAppUnits: no variant present")


def deserialize_aws_json_1_1(data: dict) -> WebAppUnits:
    if data.get("Provisioned") is not None:
        return {"Provisioned": data["Provisioned"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("WebAppUnits: no recognized variant key")
