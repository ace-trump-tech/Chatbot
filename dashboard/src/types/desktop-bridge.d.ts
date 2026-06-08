export {};

declare global {
  interface 摆烂仙君DesktopAppUpdateCheckResult {
    ok: boolean;
    reason?: string | null;
    currentVersion?: string;
    latestVersion?: string | null;
    hasUpdate: boolean;
  }

  interface 摆烂仙君DesktopAppUpdateResult {
    ok: boolean;
    reason?: string | null;
  }

  interface 摆烂仙君AppUpdaterBridge {
    checkForAppUpdate: () => Promise<摆烂仙君DesktopAppUpdateCheckResult>;
    installAppUpdate: () => Promise<摆烂仙君DesktopAppUpdateResult>;
  }

  interface Window {
    astrbotAppUpdater?: 摆烂仙君AppUpdaterBridge;
    astrbotDesktop?: {
      isDesktop: boolean;
      isDesktopRuntime: () => Promise<boolean>;
      getBackendState: () => Promise<{
        running: boolean;
        spawning: boolean;
        restarting: boolean;
        canManage: boolean;
      }>;
      restartBackend: (authToken?: string | null) => Promise<{
        ok: boolean;
        reason: string | null;
      }>;
      stopBackend: () => Promise<{
        ok: boolean;
        reason: string | null;
      }>;
      onTrayRestartBackend?: (callback: () => void) => () => void;
    };
  }
}
