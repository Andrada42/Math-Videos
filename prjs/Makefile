# PROJ ?= 'simple_ex'   it will be provided by the mk executabile

# FILE  	by default, F=main (main.py)
F ?= main
# SCENE 	we can specify the scene with S=...
S ?=
# QUALLITY 	by default, Q=l (low) => -ql flag for manim
Q ?= l

render:
	@echo "============== Render: prjs/$(PROJ) =============="
	cd "$(PROJ)" && manim -q$(Q) "$(F).py" $(S)
	@echo "============== Rendering completed =============="

clean:
	@echo "============== Clean: prjs/$(PROJ) =============="
	rm -rf "$(PROJ)/media" "$(PROJ)/__pycache__"
	@echo "============== Cleaning completed =============="
# "..." for filenames with spaces