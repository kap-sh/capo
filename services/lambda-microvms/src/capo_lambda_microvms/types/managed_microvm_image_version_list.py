"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ManagedMicrovmImageVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.managed_microvm_image_version

ManagedMicrovmImageVersionList: TypeAlias = list[
    "capo_lambda_microvms.types.managed_microvm_image_version.ManagedMicrovmImageVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedMicrovmImageVersionList) -> list:
    import capo_lambda_microvms.types.managed_microvm_image_version

    out: list = []
    for item in value:
        out.append(
            capo_lambda_microvms.types.managed_microvm_image_version.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ManagedMicrovmImageVersionList:
    import capo_lambda_microvms.types.managed_microvm_image_version

    out: ManagedMicrovmImageVersionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda_microvms.types.managed_microvm_image_version.deserialize_json(
                item
            )
        )
    return out
