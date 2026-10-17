"""Generated from Smithy shape ``com.amazonaws.lambdaweb#BuildConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.code_config
    import capo_lambda_web.types.runtime_config


class BuildConfig(TypedDict, closed=True):
    code_config: "capo_lambda_web.types.code_config.CodeConfig"
    """<p>The code configuration specifying where the deployment artifact is stored.</p>"""
    runtime_config: "capo_lambda_web.types.runtime_config.RuntimeConfig"
    """<p>The runtime configuration for the revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuildConfig) -> dict:
    out: dict = {}
    import capo_lambda_web.types.code_config

    out["codeConfig"] = capo_lambda_web.types.code_config.serialize_json(
        value["code_config"]
    )
    import capo_lambda_web.types.runtime_config

    out["runtimeConfig"] = capo_lambda_web.types.runtime_config.serialize_json(
        value["runtime_config"]
    )
    return out


def deserialize_json(data: dict) -> BuildConfig:
    out: BuildConfig = {}  # type: ignore[typeddict-item]
    if data.get("codeConfig") is not None:
        import capo_lambda_web.types.code_config

        out["code_config"] = capo_lambda_web.types.code_config.deserialize_json(
            data["codeConfig"]
        )
    else:
        raise DeserializationError("BuildConfig.code_config required")
    if data.get("runtimeConfig") is not None:
        import capo_lambda_web.types.runtime_config

        out["runtime_config"] = capo_lambda_web.types.runtime_config.deserialize_json(
            data["runtimeConfig"]
        )
    else:
        raise DeserializationError("BuildConfig.runtime_config required")
    return out
