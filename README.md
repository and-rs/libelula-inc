### AI Categorizer

1. Install uv (please install globally)
   ```
   pip install uv
   ```

2. install dependencies
   ```
   uv pip install pyproject.toml
   ```
   or
   ```
   uv sync
   ```

3. Start the app locally
   ```
   uv run fastapi dev
   ```

4. Start the TailwindCSS CLI to update css in realtime
   ```
   uv run tailwind.py
   ```

### TODO

- [ ] black, djlint and basedpyright precommit pipeline
- [ ] autoreload tailwind stylesheet
- [ ] integrate rustywind?
- [x] jinja fragments (not necessary)
