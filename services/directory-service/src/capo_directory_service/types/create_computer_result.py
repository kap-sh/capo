"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateComputerResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.computer


class CreateComputerResult(TypedDict, closed=True):
    computer: NotRequired["capo_directory_service.types.computer.Computer"]
    """<p>A <a>Computer</a> object that represents the computer account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateComputerResult) -> dict:
    out: dict = {}
    if "computer" in value:
        import capo_directory_service.types.computer

        out["Computer"] = capo_directory_service.types.computer.serialize_aws_json_1_1(
            value["computer"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateComputerResult:
    out: CreateComputerResult = {}  # type: ignore[typeddict-item]
    if data.get("Computer") is not None:
        import capo_directory_service.types.computer

        out["computer"] = (
            capo_directory_service.types.computer.deserialize_aws_json_1_1(
                data["Computer"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateComputerResult) -> dict:
    out: dict = {}
    if "computer" in value:
        import capo_directory_service.types.computer

        out["Computer"] = capo_directory_service.types.computer.serialize_cbor(
            value["computer"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateComputerResult:
    out: CreateComputerResult = {}  # type: ignore[typeddict-item]
    if data.get("Computer") is not None:
        import capo_directory_service.types.computer

        out["computer"] = capo_directory_service.types.computer.deserialize_cbor(
            data["Computer"]
        )
    return out
