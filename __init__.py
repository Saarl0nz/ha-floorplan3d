"""3D Haus: registriert das 3D-Hausplan-Panel in der Seitenleiste."""

from __future__ import annotations

import json
from pathlib import Path

from homeassistant.components import frontend, panel_custom
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import (
    CONF_TITLE,
    DEFAULT_TITLE,
    DOMAIN,
    PANEL_URL_PATH,
    STATIC_URL,
    WEBCOMPONENT,
)

_DIR = Path(__file__).parent


def _version() -> str:
    """Version aus manifest.json lesen (dient als Cache-Schlüssel der JS-Datei)."""
    try:
        return json.loads((_DIR / "manifest.json").read_text(encoding="utf-8"))["version"]
    except (OSError, KeyError, ValueError):
        return "0"


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Panel einrichten."""
    data = hass.data.setdefault(DOMAIN, {})
    if not data.get("static"):
        await hass.http.async_register_static_paths(
            [
                StaticPathConfig(
                    STATIC_URL,
                    str(_DIR / "frontend" / "floorplan3d-panel.js"),
                    False,
                )
            ]
        )
        data["static"] = True

    version = await hass.async_add_executor_job(_version)
    title = entry.options.get(CONF_TITLE) or entry.data.get(CONF_TITLE) or DEFAULT_TITLE

    await panel_custom.async_register_panel(
        hass,
        frontend_url_path=PANEL_URL_PATH,
        webcomponent_name=WEBCOMPONENT,
        sidebar_title=title,
        sidebar_icon="mdi:floor-plan",
        module_url=f"{STATIC_URL}?v={version}",
        embed_iframe=False,
        require_admin=False,
        config={"title": title},
    )
    entry.async_on_unload(entry.add_update_listener(_async_reload))
    return True


async def _async_reload(hass: HomeAssistant, entry: ConfigEntry) -> None:
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Panel wieder entfernen."""
    frontend.async_remove_panel(hass, PANEL_URL_PATH, warn_if_unknown=False)
    return True
