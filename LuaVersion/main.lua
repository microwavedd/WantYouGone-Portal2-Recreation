-- Carga la música

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
local function typewriterEffect(text, x, y, delay)
    local displayedText = ""
    local timer = coroutine.create(function()
        for i = 1, #text do
            displayedText = string.sub(text, 1, i)
            love.timer.sleep(delay)
            coroutine.yield(displayedText)
        end
    end)

    while coroutine.status(timer) ~= "dead" do
        local _, partialText = coroutine.resume(timer)
        love.graphics.print(partialText, x, y)
        love.graphics.present()  -- Update the screen to show the partial text
    end
end

function clearScreen()
    love.graphics.setColor(0, 0, 0)  -- Set color to black
    love.graphics.rectangle("fill", 0, 0, love.graphics.getWidth(), love.graphics.getHeight())  -- Draw a black rectangle covering the entire screen
    clear = 1
    sleep(0.3)
    clear = 0
end

function love.load()
    music = love.audio.newSource("WantYouGone.mp3", "stream")
    aperture = love.graphics.newImage("apertutrer.png")
    nums = love.graphics.newImage("aperturenums.png")
    matrix = love.graphics.newImage("aperturematrix.png")
end

-- Reproduce la música cuando se inicie el juego
function love.update(dt)
    love.audio.play(music)
    
end
function love.draw()
    -- Obtiene las dimensiones de la ventana
    local windowWidth = love.graphics.getWidth()
    local windowHeight = love.graphics.getHeight()

    -- Calcula las coordenadas para la esquina superior derecha
    local x = windowWidth - aperture:getWidth()
    local y = 0
    function images()
        love.graphics.draw(aperture,x + 90 ,y,0,0.5,0.5)
        love.graphics.draw(nums,x + 40 ,y - 2.5,0,0.5,0.5)
        love.graphics.draw(matrix,x - 150,y,0,0.5,0.5)
    end
    images()
    while clear == 0 do
        if clear == 1 then
            images()
        end
    end
end
function sleep(n)
    love.timer.sleep(n)
end









