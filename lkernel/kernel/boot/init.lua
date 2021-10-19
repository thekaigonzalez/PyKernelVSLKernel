local boot = {}

boot.order = {}

function boot:create_new_boot(name, init)
    boot.order[#boot.order+1] = {name=name, init=init}
end

return boot