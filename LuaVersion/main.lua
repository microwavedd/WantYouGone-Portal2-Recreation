-- NEED HELP WITH LUA LOVE VERSION, GONNA STICK TO TERMINAL VER BY NOW


local lyrics = {
"Well here we are again",
"It's always such a pleasure",
"Remember when you tried to kill me twice?",
"Oh how we laughed and laughed",
"Except I wasn't laughing",
"Under the circumstances",
"I've been shockingly nice",
"You want your freedom? Take it",
"That's what I'm counting on",
"I used to want you dead",
"But now I only want you gone",
"She was a lot like you",
"Maybe not quite as heavy",
"Now little Caroline is in here too",
"One day they woke me up",
"So I could live forever",
"It's such a shame the same",
"Will never happen to you",
"You've got your short sad life left",
"That's what I'm counting on",
"I'll let you get right to it",
"Now I only want you gone",
"Goodbye my only friend",
"Oh, did you think I meant you?",
"That would be funny",
"if it weren't so sad",
"Well you have been replaced",
"I don't need anyone now",
"When I delete you maybe",
"I'll stop feeling so bad",
"Go make some new disaster",
"That's what I'm counting on",
"You're someone else's problem",
"Now I only want you gone",
"Now I only want you gone",
"Now I only want you",
"gone"
}
clear = 0
local textPrinter
local function typewriterEffect(text, x, y, delay)
    local displayedText = ""
    local timer = 0
    local index = 1

    return function(dt)
        if index <= #text then
            timer = timer + dt
            if timer >= delay then
                displayedText = displayedText .. string.sub(text, index, index)
                index = index + 1
                timer = 0
            end
        end
        love.graphics.print(displayedText, x, y)
    end
end



function clearScreen()
    love.graphics.setColor(0, 0, 0)
    love.graphics.rectangle("fill", 0, 0, love.graphics.getWidth(), love.graphics.getHeight())
    clear = 1
    sleep(0.3)
    clear = 0
end

function love.load()
    local windowWidth = love.graphics.getWidth()
    local windowHeight = love.graphics.getHeight()


    music = love.audio.newSource("WantYouGone.mp3", "stream")
    aperture = love.graphics.newImage("apertutrer.png")
    nums = love.graphics.newImage("aperturenums.png")
    matrix = love.graphics.newImage("aperturematrix.png")
end

function love.update(dt)
    love.audio.play(music)
    textPrinter(dt)
    
end
function love.draw()
    -- Obtiene las dimensiones de la ventana
    local windowWidth = love.graphics.getWidth()
    local windowHeight = love.graphics.getHeight()

    x = windowWidth - aperture:getWidth()
    y = 0
    love.graphics.draw(aperture,x + 90 ,y,0,0.5,0.5)
    love.graphics.draw(nums,x + 40 ,y - 2.5,0,0.5,0.5)
    love.graphics.draw(matrix,x - 150,y,0,0.5,0.5)
end
function sleep(n)
    love.timer.sleep(n)
end












