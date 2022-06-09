local status_ok, configs = pcall(require, "nvim-treesitter.configs")
if not status_ok then
  return
end

configs.setup {
  ensure_installed = "bash c c_sharp cmake comment cpp css dockerfile fennel go help html http javascript json json5 jsonc latex lua kotlin markdown ninja norg perl php python rasi rst regex scss solidity svelte tsx typescript vim vue yaml zig", -- one of "all", "maintained" (parsers with maintainers), or a list of languages
  sync_install = true, -- install languages synchronously (only applied to `ensure_installed`)
  ignore_install = { "" }, -- List of parsers to ignore installing
  autopairs = {
    enable = true,
  },
  highlight = {
    enable = true, -- false will disable the whole extension
    disable = { "" }, -- list of language that will be disabled
    additional_vim_regex_highlighting = true,
  },
  indent = { enable = true, disable = { "yaml" } },
  context_commentstring = {
    enable = true,
    enable_autocmd = false,
  },
}
