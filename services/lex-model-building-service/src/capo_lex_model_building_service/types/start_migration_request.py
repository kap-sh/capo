"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#StartMigrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.iam_role_arn
    import capo_lex_model_building_service.types.migration_strategy
    import capo_lex_model_building_service.types.v2_bot_name
    import capo_lex_model_building_service.types.version


class StartMigrationRequest(TypedDict, closed=True):
    v1_bot_name: "capo_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the Amazon Lex V1 bot that you are migrating to Amazon Lex V2.</p>"""
    v1_bot_version: "capo_lex_model_building_service.types.version.Version"
    """<p>The version of the bot to migrate to Amazon Lex V2. You can migrate the <code>$LATEST</code> version as well as any numbered version.</p>"""
    v2_bot_name: "capo_lex_model_building_service.types.v2_bot_name.V2BotName"
    """<p>The name of the Amazon Lex V2 bot that you are migrating the Amazon Lex V1 bot to. </p> <ul> <li> <p>If the Amazon Lex V2 bot doesn't exist, you must use the <code>CREATE_NEW</code> migration strategy.</p> </li> <li> <p>If the Amazon Lex V2 bot exists, you must use the <code>UPDATE_EXISTING</code> migration strategy to change the contents of the Amazon Lex V2 bot.</p> </li> </ul>"""
    v2_bot_role: "capo_lex_model_building_service.types.iam_role_arn.IamRoleArn"
    """<p>The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.</p>"""
    migration_strategy: (
        "capo_lex_model_building_service.types.migration_strategy.MigrationStrategy"
    )
    """<p>The strategy used to conduct the migration.</p> <ul> <li> <p> <code>CREATE_NEW</code> - Creates a new Amazon Lex V2 bot and migrates the Amazon Lex V1 bot to the new bot.</p> </li> <li> <p> <code>UPDATE_EXISTING</code> - Overwrites the existing Amazon Lex V2 bot metadata and the locale being migrated. It doesn't change any other locales in the Amazon Lex V2 bot. If the locale doesn't exist, a new locale is created in the Amazon Lex V2 bot.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMigrationRequest) -> dict:
    out: dict = {}
    out["v1BotName"] = value["v1_bot_name"]
    out["v1BotVersion"] = value["v1_bot_version"]
    out["v2BotName"] = value["v2_bot_name"]
    out["v2BotRole"] = value["v2_bot_role"]
    import capo_lex_model_building_service.types.migration_strategy

    out["migrationStrategy"] = (
        capo_lex_model_building_service.types.migration_strategy.serialize_json(
            value["migration_strategy"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartMigrationRequest:
    out: StartMigrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("v1BotName") is not None:
        out["v1_bot_name"] = data["v1BotName"]
    else:
        out["v1_bot_name"] = ""
    if data.get("v1BotVersion") is not None:
        out["v1_bot_version"] = data["v1BotVersion"]
    else:
        out["v1_bot_version"] = ""
    if data.get("v2BotName") is not None:
        out["v2_bot_name"] = data["v2BotName"]
    else:
        out["v2_bot_name"] = ""
    if data.get("v2BotRole") is not None:
        out["v2_bot_role"] = data["v2BotRole"]
    else:
        out["v2_bot_role"] = ""
    if data.get("migrationStrategy") is not None:
        import capo_lex_model_building_service.types.migration_strategy

        out["migration_strategy"] = (
            capo_lex_model_building_service.types.migration_strategy.deserialize_json(
                data["migrationStrategy"]
            )
        )
    else:
        import typing

        out["migration_strategy"] = typing.cast(
            "capo_lex_model_building_service.types.migration_strategy.MigrationStrategy",
            "",
        )
    return out
