"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateScriptOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.script


class UpdateScriptOutput(TypedDict, closed=True):
    script: NotRequired["capo_gamelift.types.script.Script"]
    """<p>The newly created script record with a unique script ID. The new script's storage location reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your account, the storage location reflects the information that was provided in the <i>CreateScript</i> request; (2) If the script file was uploaded from a local zip file, the storage location reflects an S3 location controlled by the Amazon GameLift Servers service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateScriptOutput) -> dict:
    out: dict = {}
    if "script" in value:
        import capo_gamelift.types.script

        out["Script"] = capo_gamelift.types.script.serialize_aws_json_1_1(
            value["script"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateScriptOutput:
    out: UpdateScriptOutput = {}  # type: ignore[typeddict-item]
    if data.get("Script") is not None:
        import capo_gamelift.types.script

        out["script"] = capo_gamelift.types.script.deserialize_aws_json_1_1(
            data["Script"]
        )
    return out
