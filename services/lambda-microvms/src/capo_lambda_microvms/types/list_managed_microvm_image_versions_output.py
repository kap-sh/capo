"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListManagedMicrovmImageVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.managed_microvm_image_version_list
    import capo_lambda_microvms.types.string


class ListManagedMicrovmImageVersionsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_lambda_microvms.types.string.String"]
    """<p>The pagination token to use in a subsequent request to retrieve the next page of results. This value is null when there are no more results to return.</p>"""
    items: "capo_lambda_microvms.types.managed_microvm_image_version_list.ManagedMicrovmImageVersionList"
    """<p>The list of managed MicroVM image versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedMicrovmImageVersionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_lambda_microvms.types.managed_microvm_image_version_list

    out["items"] = (
        capo_lambda_microvms.types.managed_microvm_image_version_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListManagedMicrovmImageVersionsOutput:
    out: ListManagedMicrovmImageVersionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("items") is not None:
        import capo_lambda_microvms.types.managed_microvm_image_version_list

        out["items"] = (
            capo_lambda_microvms.types.managed_microvm_image_version_list.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError(
            "ListManagedMicrovmImageVersionsOutput.items required"
        )
    return out
