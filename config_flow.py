"""Einrichtung über die Oberfläche (ein Klick, keine Eingaben nötig)."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import CONF_TITLE, DEFAULT_TITLE, DOMAIN


class Floorplan3dConfigFlow(ConfigFlow, domain=DOMAIN):
    """Ein Eintrag genügt: er legt das Panel in der Seitenleiste an."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        return self.async_create_entry(
            title=DEFAULT_TITLE, data={CONF_TITLE: DEFAULT_TITLE}
        )
