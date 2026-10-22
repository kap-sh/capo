"""Generated from Smithy shape ``com.amazonaws.dynamodb#DisassociationProtectionEnabled``."""

from typing import TypeAlias

"""<p>Specifies whether a global table replica is protected from disassociation. While protection is enabled, <code>UpdateTable</code> rejects requests to disassociate the replica. Disassociation protection is enabled by default and is independent of deletion protection.</p>"""
DisassociationProtectionEnabled: TypeAlias = bool
