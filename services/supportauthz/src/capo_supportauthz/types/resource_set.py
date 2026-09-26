"""Generated from Smithy shape ``com.amazonaws.supportauthz#ResourceSet``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_supportauthz.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_supportauthz.types.resources


class _ResourceSet_allResourcesInRegion(TypedDict, closed=True):
    allResourcesInRegion: "None"


class _ResourceSet_resources(TypedDict, closed=True):
    resources: "capo_supportauthz.types.resources.Resources"


ResourceSet: TypeAlias = _ResourceSet_allResourcesInRegion | _ResourceSet_resources


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSet) -> dict:
    if "allResourcesInRegion" in value:
        return {"allResourcesInRegion": {}}
    elif "resources" in value:
        import capo_supportauthz.types.resources

        return {
            "resources": capo_supportauthz.types.resources.serialize_json(
                value["resources"]
            )
        }
    else:
        raise SerializationError("ResourceSet: no variant present")


def deserialize_json(data: dict) -> ResourceSet:
    if data.get("allResourcesInRegion") is not None:
        return {"allResourcesInRegion": None}
    elif data.get("resources") is not None:
        import capo_supportauthz.types.resources

        return {
            "resources": capo_supportauthz.types.resources.deserialize_json(
                data["resources"]
            )
        }
    else:
        raise DeserializationError("ResourceSet: no recognized variant key")
