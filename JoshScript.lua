local floor = math.floor;
local rep = string.rep;

local value = 0;

local function err(msg)
	print("JoshScript Error // "..msg);
end

local function interpret(code)
	if #code % 4 ~= 0 or not code:lower():match(rep("josh", floor(#code/4))) then
		err("Code is not 100% josh, ensure there is no unintended spacing.");
		return;
	end
	
	for josh in code:gmatch("....") do
		if josh == "JOSH" then
			value = value + 1;
		elseif josh == "josh" then
			value = value - (value > 0 and 1 or 0);
		elseif josh == "Josh" then
			value = value * 2;
		elseif josh == "josH" then
			value = floor(value / 2);
		elseif josh == "JOsh" then
			io.write(string.char(value));
		elseif josh == "jOsh" then
			value = 0;
		elseif josh == "JOSh" then
			value = value ^ 2;
		elseif josh == "joSH" then
			io.write("\nIN> ");
			local c = io.read(1);
			value = c:byte();
		else
			err("Not a valid josh");
			return;
		end
	end
end

io.write("JoshScript v1.02\n> ");

local file = io.open(arg[1]);
interpret(file:read("*all"));

io.write("\n");
