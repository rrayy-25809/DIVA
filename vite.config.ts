import { defineConfig } from "vite";
import { resolve } from "path";
import { readdirSync } from "fs";

const pagesDir = resolve(__dirname, 'client');
const htmlFiles = readdirSync(pagesDir).filter(file => file.endsWith('.html'));
const input = htmlFiles.reduce<Record<string, string>>((acc, file) => {
    const name = file.replace('.html', '');
    acc[name] = resolve(pagesDir, file);
    return acc;
}, {});

// 콘솔 경고 메시지 필터링 플러그인
function ignoreModuleLevelDirectivesWarnings() {
    return {
        name: 'ignore-module-level-directives-warnings',
        apply: "build" as const,
        buildStart() {
            const origWarn = console.warn;
            console.warn = function (...args) {
                if (
                    args.length > 0 &&
                    typeof args[0] === 'string' &&
                    args[0].includes('Module level directives cause errors when bundled')
                ) {
                    return;
                }
                origWarn.apply(console, args);
            };
        }
    };
}

export default defineConfig({
    build: {
        rollupOptions: {
            input
        }
    },
    plugins: [
        ignoreModuleLevelDirectivesWarnings()
    ]
});