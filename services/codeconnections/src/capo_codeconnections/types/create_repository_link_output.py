"""Generated from Smithy shape ``com.amazonaws.codeconnections#CreateRepositoryLinkOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeconnections.types.repository_link_info


class CreateRepositoryLinkOutput(TypedDict, closed=True):
    repository_link_info: (
        "capo_codeconnections.types.repository_link_info.RepositoryLinkInfo"
    )
    """<p>The returned information about the created repository link.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRepositoryLinkOutput) -> dict:
    out: dict = {}
    import capo_codeconnections.types.repository_link_info

    out["RepositoryLinkInfo"] = (
        capo_codeconnections.types.repository_link_info.serialize_aws_json_1_0(
            value["repository_link_info"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRepositoryLinkOutput:
    out: CreateRepositoryLinkOutput = {}  # type: ignore[typeddict-item]
    if data.get("RepositoryLinkInfo") is not None:
        import capo_codeconnections.types.repository_link_info

        out["repository_link_info"] = (
            capo_codeconnections.types.repository_link_info.deserialize_aws_json_1_0(
                data["RepositoryLinkInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRepositoryLinkOutput.repository_link_info required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateRepositoryLinkOutput) -> dict:
    out: dict = {}
    import capo_codeconnections.types.repository_link_info

    out["RepositoryLinkInfo"] = (
        capo_codeconnections.types.repository_link_info.serialize_cbor(
            value["repository_link_info"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> CreateRepositoryLinkOutput:
    out: CreateRepositoryLinkOutput = {}  # type: ignore[typeddict-item]
    if data.get("RepositoryLinkInfo") is not None:
        import capo_codeconnections.types.repository_link_info

        out["repository_link_info"] = (
            capo_codeconnections.types.repository_link_info.deserialize_cbor(
                data["RepositoryLinkInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRepositoryLinkOutput.repository_link_info required"
        )
    return out
